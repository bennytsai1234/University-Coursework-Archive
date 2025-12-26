package com.example.sharedpreferences;

import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.Preference;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private Button btnEnd, btnClear;
    private TextView txtName, edtName;
    private SharedPreferences preference;
    private String sname;
    private String msg;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtName = findViewById(R.id.textView);
        edtName = findViewById(R.id.editTextText2);
        btnEnd = findViewById(R.id.btnEnd);
        btnClear = findViewById(R.id.btnClear);

        btnEnd.setOnClickListener(listener);
        btnClear.setOnClickListener(listener);

        preference = getSharedPreferences("preFile", MODE_PRIVATE);
        sname = preference.getString("name", "");

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
                .setPositiveButton("確定", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {

                    }
                }).show();
    }

    private View.OnClickListener listener = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            switch(view.getId()){
                case R.id.btnEnd:
                    finish();
                    break;
                case R.id.btnClear:
                    if(!sname.equals("")){
                        preference.edit().clear().commit();
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
                    .commit();
        }
    }
}