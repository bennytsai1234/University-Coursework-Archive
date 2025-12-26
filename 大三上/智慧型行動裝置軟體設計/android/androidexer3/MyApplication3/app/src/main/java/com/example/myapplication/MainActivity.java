package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.media.AudioManager;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.view.Surface;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.VideoView;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private String videoname;
    private Button btn1,btn2,btnend,btnrev,btnstop,btnfast;
    private SurfaceView surfaceView;
    private SurfaceHolder surfaceHolder;
    private MediaPlayer mediaPlayer;
    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn1 = findViewById(R.id.button);
        btn2 = findViewById(R.id.button2);
        btnend = findViewById(R.id.button3);
        btnrev = findViewById(R.id.button4);
        btnstop = findViewById(R.id.button5);
        btnfast = findViewById(R.id.button6);
        textView = findViewById(R.id.TestView);

        btn1.setOnClickListener(btnlistener);
        btn2.setOnClickListener(btnlistener);
        btnend.setOnClickListener(btnlistener);
        btnfast.setOnClickListener(btnlistener);
        btnstop.setOnClickListener(btnlistener);
        btnrev.setOnClickListener(btnlistener);

        surfaceView = findViewById(R.id.surfaceView);
        mediaPlayer = new MediaPlayer();
        surfaceHolder = surfaceView.getHolder();

    }

    private View.OnClickListener btnlistener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            int nowt;
            String filepath="android.resource://" + getPackageName() + "/";
            switch (v.getId()){
                case R.id.button:
                    videoname = "vd1";//"never gonna give you up.mp4";
                    Uri uri = Uri.parse(filepath+ R.raw.vd1);
                    mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
                    mediaPlayer.setDisplay(surfaceHolder);
                    try {
                        mediaPlayer.reset();
                        mediaPlayer.setDataSource(getApplicationContext(),uri);
                        mediaPlayer.prepare();
                        mediaPlayer.start();
                    }catch (IOException e) {}
                    break;
                case R.id.button2:
                    videoname = "vd2";//"粛聖!!ロリ神レクイエム.mp4";
                    Uri uri2 = Uri.parse(filepath+ R.raw.vd2);

                    mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
                    mediaPlayer.setDisplay(surfaceHolder);
                    try {
                        mediaPlayer.reset();
                        mediaPlayer.setDataSource(getApplicationContext(),uri2);
                        mediaPlayer.prepare();
                        mediaPlayer.start();
                    }catch (IOException e) {}
                    break;
                case R.id.button3:
                    finish();
                    break;
                case R.id.button5:
                    if(mediaPlayer.isPlaying())mediaPlayer.pause();
                    else mediaPlayer.start();
                    break;
                case R.id.button4:
                    nowt = (mediaPlayer.getCurrentPosition()-5000);//5 second
                    if(nowt < 0) nowt = 0;
                    mediaPlayer.seekTo(nowt);
                    textView.setText("倒轉");
                    break;
                case R.id.button6:
                    nowt = (mediaPlayer.getCurrentPosition()+5000);
                    if(nowt > mediaPlayer.getDuration()) nowt = mediaPlayer.getDuration();
                    mediaPlayer.seekTo(nowt);
                    textView.setText("快轉");
                    break;
            }
            mediaPlayer.setOnCompletionListener(new MediaPlayer.OnCompletionListener() {
                @Override
                public void onCompletion(MediaPlayer mp) {
                    textView.setText(videoname+"播放結束");
                }
            });
            mediaPlayer.setOnPreparedListener(new MediaPlayer.OnPreparedListener() {
                @Override
                public void onPrepared(MediaPlayer mp) {
                    textView.setText("正在播放 : "+videoname+"\n");
                }
            });
        }
    };

}