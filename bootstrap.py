from pathlib import Path
root=Path(__file__).parent
files={
'settings.gradle': '''pluginManagement { repositories { google(); mavenCentral(); gradlePluginPortal() } }
dependencyResolutionManagement { repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS); repositories { google(); mavenCentral() } }
rootProject.name = 'AndroidForge'
include ':app', ':core'
''',
'build.gradle': '''plugins { id 'com.android.application' version '8.7.3' apply false }
''',
'gradle.properties': '''org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
org.gradle.parallel=false
android.useAndroidX=false
''',
'core/build.gradle': '''plugins { id 'java-library' }
java { sourceCompatibility = JavaVersion.VERSION_17; targetCompatibility = JavaVersion.VERSION_17 }
dependencies { testImplementation 'junit:junit:4.13.2' }
''',
'app/build.gradle': '''plugins { id 'com.android.application' }
android {
    namespace 'dev.androidforge'
    compileSdk 35
    defaultConfig { applicationId 'dev.androidforge'; minSdk 29; targetSdk 35; versionCode 1; versionName '0.1.0'; testInstrumentationRunner 'android.test.InstrumentationTestRunner' }
    compileOptions { sourceCompatibility JavaVersion.VERSION_17; targetCompatibility JavaVersion.VERSION_17 }
    buildTypes { release { minifyEnabled false } }
}
dependencies { implementation project(':core') }
''',
'app/src/main/AndroidManifest.xml': '''<manifest xmlns:android="http://schemas.android.com/apk/res/android">
<application android:name=".ForgeApp" android:label="Android Forge" android:theme="@style/AppTheme" android:icon="@drawable/ic_forge" android:allowBackup="false" android:supportsRtl="true" android:usesCleartextTraffic="false">
<activity android:name=".ui.PreviewActivity" android:exported="false"/>
<activity android:name=".ui.EditorActivity" android:exported="false" android:windowSoftInputMode="adjustResize"/>
<activity android:name=".ui.ProjectActivity" android:exported="false"/>
<activity android:name=".ui.MainActivity" android:exported="true"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity>
</application></manifest>
''',
'app/src/main/res/values/styles.xml': '''<resources><style name="AppTheme" parent="android:style/Theme.Material.NoActionBar"><item name="android:fontFamily">sans</item><item name="android:windowLightStatusBar">false</item><item name="android:statusBarColor">#0C1220</item><item name="android:navigationBarColor">#0C1220</item><item name="android:colorAccent">#65DCAC</item><item name="android:windowActionModeOverlay">true</item><item name="android:windowLightNavigationBar">false</item><item name="android:windowBackground">#0C1220</item></style></resources>
''',
'app/src/main/res/drawable/ic_forge.xml': '''<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="108dp" android:height="108dp" android:viewportWidth="108" android:viewportHeight="108"><path android:fillColor="#0C1220" android:pathData="M0,0h108v108h-108z"/><path android:fillColor="#65DCAC" android:pathData="M31,28h49l-8,14h-27v12h23l-8,14h-15v15h-14z"/><path android:fillColor="#DCEAE5" android:pathData="M67,70h12v13h-20z"/></vector>
''',
'.gitignore': '''.gradle/
**/build/
local.properties
*.jks
*.keystore
editor/node_modules/
''',
'editor/package.json': '''{"name":"android-forge-editor","private":true,"version":"0.1.0","scripts":{"build":"esbuild editor.js --bundle --minify --target=chrome80 --outfile=../app/src/main/assets/editor/editor.js"},"dependencies":{"codemirror":"^6.0.1","@codemirror/lang-java":"^6.0.2","@codemirror/lang-javascript":"^6.2.2","@codemirror/lang-xml":"^6.1.0","@codemirror/lang-json":"^6.0.1","@codemirror/lang-css":"^6.3.1","@codemirror/lang-html":"^6.4.9","@codemirror/lang-markdown":"^6.3.3","@codemirror/legacy-modes":"^6.4.0","@codemirror/theme-one-dark":"^6.1.2","@codemirror/merge":"^6.10.1","esbuild":"^0.25.0"}}
'''
}
for path,text in files.items():
 p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
(root/'local.properties').write_text('sdk.dir=/home/ubuntu/android-sdk\n')
print('Native Gradle skeleton ready')
