package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.TextView;
import android.widget.VideoView;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    private String videoname;
    private VideoView videoView;
    private Button btn1,btn2,btnend;
    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn1 = findViewById(R.id.button);
        btn2 =  findViewById(R.id.button2);
        btnend = findViewById(R.id.button3);
        videoView = findViewById(R.id.videoView);
        textView = findViewById(R.id.TestView);

        btn1.setOnClickListener(btnlistener);
        btn2.setOnClickListener(btnlistener);
        btnend.setOnClickListener(btnlistener);

        videoView.setMediaController(new MediaController(MainActivity.this));
        videoView.setOnCompletionListener(completionlistener);
        videoView.setOnPreparedListener(preparedListener);

    }

    private View.OnClickListener btnlistener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            String filepath="android.resource://" + getPackageName() + "/";
            switch (v.getId()){
                case R.id.button:
                    videoname = "vd1";
                    Uri uri = Uri.parse(filepath+ R.raw.vd1);
                    videoView.setVideoURI(uri);
                    videoView.start();
                    break;
                case R.id.button2:
                    videoname = "vd2";
                    Uri uri2 = Uri.parse(filepath+ R.raw.vd2);
                    videoView.setVideoURI(uri2);
                    videoView.start();
                    break;
                case R.id.button3:
                    finish();
                    break;
            }
        }
    };

    private MediaPlayer.OnPreparedListener preparedListener = new MediaPlayer.OnPreparedListener() {
        @Override
        public void onPrepared(MediaPlayer mp) {
            textView.setText("正在播放 : "+videoname+"\n");
        }
    };

    private MediaPlayer.OnCompletionListener completionlistener = new MediaPlayer.OnCompletionListener() {
        @Override
        public void onCompletion(MediaPlayer mp) {

            textView.setText(videoname+"播放結束");

        }
    };

}