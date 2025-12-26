package com.example.ch7;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private ListView listPrefer;
    private TextView myTextview;
    private Button myBtn;
    int count;
    String[] Balls=new String[]{"籃球","足球","棒球","其他"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myBtn=findViewById(R.id.button2);
        listPrefer=findViewById(R.id.lstPrefer);
        myTextview=findViewById(R.id.textView2);
        ArrayAdapter<String> adapterBalls= new ArrayAdapter<>(this, android.R.layout.simple_list_item_multiple_choice, Balls);
        listPrefer.setChoiceMode(ListView.CHOICE_MODE_MULTIPLE);
        listPrefer.setAdapter(adapterBalls);
        listPrefer.setOnItemClickListener(listPreferListener);
        listPrefer.setSelector(R.drawable.classicbubbletea);
        listPrefer.setTextFilterEnabled(true);
        count=adapterBalls.getCount();
        myBtn.setOnClickListener(myBtnListener);
    }
    private View.OnClickListener myBtnListener=new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            String selAll="";
            for (int p=0;p<count;p++){
                if(listPrefer.isItemChecked(p))
                    selAll+=Balls[p]+" ";
            }
            myTextview.setText("我最喜歡的運動是:"+ selAll);
        }
    };
    private final AdapterView.OnItemClickListener listPreferListener =new AdapterView.OnItemClickListener() {
        @SuppressLint("SetTextI18n")
        @Override
        public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
            String sel= listPrefer.getItemAtPosition(i).toString();
            myTextview.setText("我最喜歡的運動是:"+ sel);
        }
    };
}