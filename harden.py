from pathlib import Path
r=Path(__file__).parent
p=r/'core/build.gradle';s=p.read_text().replace("dependencies { testImplementation", "dependencies { api 'com.google.re2j:re2j:1.8'; testImplementation");p.write_text(s)
p=r/'core/src/main/java/dev/androidforge/core/Workspace.java';s=p.read_text().replace('import java.util.regex.*;','import com.google.re2j.*;').replace('Files.deleteIfExists(draft(id,path).toPath()); }\n    public synchronized File backup', 'SafeFiles.deleteTree(draft(id,path)); }\n    public synchronized File backup');p.write_text(s)
p=r/'core/src/main/java/dev/androidforge/core/Analyzer.java';s=p.read_text().replace('if(text.contains("com.android.application")||text.contains("com.android.library")){r.modules++;if(r.gradle.isEmpty()&&!path.equals("build.gradle")&&!path.equals("build.gradle.kts"))r.gradle=path;}', 'if((text.contains("com.android.application")||text.contains("com.android.library"))&&!text.contains("apply false")){r.modules++;if(r.gradle.isEmpty())r.gradle=path;}');p.write_text(s)
p=r/'app/src/main/AndroidManifest.xml';s=p.read_text().replace('<activity android:name=', '<activity android:configChanges="orientation|screenSize|keyboardHidden" android:name=');p.write_text(s)
p=r/'app/src/main/java/dev/androidforge/ui/EditorActivity.java';s=p.read_text().replace('settings.setSupportMultipleWindows(false);','settings.setSupportMultipleWindows(false);if((getApplicationInfo().flags & android.content.pm.ApplicationInfo.FLAG_DEBUGGABLE)!=0)WebView.setWebContentsDebuggingEnabled(true);');p.write_text(s)
print('Security and lifecycle corrections applied')
