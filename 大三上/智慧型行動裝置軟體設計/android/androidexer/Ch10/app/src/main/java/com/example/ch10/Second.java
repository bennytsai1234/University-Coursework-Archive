package com.example.ch10;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class Second extends AppCompatActivity {
    private Button btn;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout);
        btn=findViewById(R.id.button4);
        btn.setOnClickListener(secondClickListener);
    }
    private View.OnClickListener secondClickListener=new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            finish();
        }
    };
}
