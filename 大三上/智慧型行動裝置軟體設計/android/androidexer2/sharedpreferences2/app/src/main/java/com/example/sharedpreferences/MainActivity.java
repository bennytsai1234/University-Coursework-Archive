package com.example.sharedpreferences;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private Button btnClear;
    private TextView edtName;
    private SharedPreferences preference;
    private String sname;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView txtName = findViewById(R.id.textView);
        edtName = findViewById(R.id.editTextText2);
        Button btnEnd = findViewById(R.id.btnEnd);
        btnClear = findViewById(R.id.btnClear);

        btnEnd.setOnClickListener(listener);
        btnClear.setOnClickListener(listener);

        preference = getSharedPreferences("preFile", MODE_PRIVATE);
        sname = preference.getString("name", "");

        String msg;
        if(sname.equals("")){  //沒有資料
            txtName.setVisibility(TextView.VISIBLE);
            edtName.setVisibility(TextView.VISIBLE);
            btnClear.setVisibility(Button.INVISIBLE);
            msg = "歡迎使用本應用程式!\n您尚未建立資料，請輸入姓名!";
        }
        else{                  //有資料
            txtName.setVisibility(TextView.INVISIBLE);
            edtName.setVisibility(TextView.INVISIBLE);
            msg = "親愛的 " + sname + "，你好!\n歡迎使用本應用程式";
        }

        //跳出歡迎視窗
        new AlertDialog.Builder(MainActivity.this)
                .setTitle("歡迎使用本軟體!")
                .setMessage(msg)
                .setPositiveButton("確定", (dialogInterface, i) -> {

                }).show();
    }

    private final View.OnClickListener listener = new View.OnClickListener() {
        @SuppressLint("NonConstantResourceId")
        @Override
        public void onClick(View view) {
            switch(view.getId()){
                case R.id.btnEnd:
                    finish();
                    break;
                case R.id.btnClear:
                    if(!sname.equals("")){
                        preference.edit().clear().apply();
                        Toast.makeText(getApplicationContext(), "所有資料已清除!", Toast.LENGTH_LONG).show();
                    }
                    btnClear.setVisibility(Button.INVISIBLE);
                    break;
            }
        }
    };


    @Override
    protected void onStop() {
        super.onStop();
        if(sname.equals("")){
            preference.edit()
                    .putString("name", edtName.getText().toString())
                    .apply();
        }
    }
}