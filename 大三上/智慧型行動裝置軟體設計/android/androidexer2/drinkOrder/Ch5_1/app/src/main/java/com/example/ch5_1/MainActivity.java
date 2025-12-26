package com.example.ch5_1;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private CheckBox myChkBox;
    private CheckBox myChkBox2;
    private CheckBox myChkBox3;
    private TextView myTxtView, myTxtView2;

    String[] Balls=new String[]{"full sugar","half sugar","no sugar"};
    int []imgid={R.drawable.bubbletea, R.drawable.greentea, R.drawable.milktea};
    private ImageView myImgView;
    int picIndex=0;
    int imgCount= imgid.length;
    private int amount=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myChkBox = findViewById(R.id.checkBox11);
        myChkBox2 = findViewById(R.id.checkBox5);
        myChkBox3 = findViewById(R.id.checkBox6);
        myTxtView = findViewById(R.id.textView6);
        RadioGroup myRadioGroup = findViewById(R.id.deliver);
        myTxtView2 = findViewById(R.id.textView2);
        Spinner spinner = findViewById(R.id.spinner);
        ArrayAdapter<String>adapterBalls=
                new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, Balls);
        adapterBalls.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapterBalls);
        spinner.setOnItemSelectedListener(spnListener);
        myChkBox.setOnCheckedChangeListener(myCheckBoxListener);
        myChkBox2.setOnCheckedChangeListener(myCheckBoxListener);
        myChkBox3.setOnCheckedChangeListener(myCheckBoxListener);
        myRadioGroup.setOnCheckedChangeListener(myRadioGruopListener);
        Button previousBtn = findViewById(R.id.button2);
        Button nextBtn = findViewById(R.id.button3);
        myImgView=findViewById(R.id.imageView);
        previousBtn.setOnClickListener(prevBtnListener);
        nextBtn.setOnClickListener(nextBtnListener);
    }
    private final View.OnClickListener nextBtnListener=
            new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                picIndex++;
                if (picIndex > imgCount-1) {
                        picIndex = 0;
                    }
                myImgView.setImageResource(imgid[picIndex]);
                }
            };
    private final View.OnClickListener prevBtnListener=
            new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    picIndex--;
                    if (picIndex < 0) {
                        picIndex = imgCount-1;
                    }
                    myImgView.setImageResource(imgid[picIndex]);
                }
            };
    private final AdapterView.OnItemSelectedListener spnListener=
            new AdapterView.OnItemSelectedListener() {
                @Override
                public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                    String sel=adapterView.getSelectedItem().toString();
                    myTxtView2.setText(sel);
                }

                @Override
                public void onNothingSelected(AdapterView<?> adapterView) {

                }
            };
    private final RadioGroup.OnCheckedChangeListener myRadioGruopListener = new RadioGroup.OnCheckedChangeListener() {
        @Override
        public void onCheckedChanged(RadioGroup group, int checkedId) {
            if(checkedId == R.id.radioButton2)
                myTxtView2.setText("內用");
            else if(checkedId == R.id.radioButton3)
                myTxtView2.setText("外帶");
        }
    };
    private final CompoundButton.OnCheckedChangeListener myCheckBoxListener = new CompoundButton.OnCheckedChangeListener() {
        @SuppressLint({"SetTextI18n", "NonConstantResourceId"})
        @Override
        public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
            switch (buttonView.getId()){
                case R.id.checkBox11:
                        if(myChkBox.isChecked()) amount += 40;
                        else amount -=40;
                        myTxtView.setText("總金額:" + amount);
                    break;
                case R.id.checkBox5:
                    if(myChkBox2.isChecked()) amount += 40;
                    else amount -=40;
                    myTxtView.setText("總金額:" + amount);
                    break;
                case R.id.checkBox6:
                    if(myChkBox3.isChecked()) amount += 15;
                    else amount -=15;
                    myTxtView.setText("總金額:" + amount);
                    break;
            }
        }
    };
}