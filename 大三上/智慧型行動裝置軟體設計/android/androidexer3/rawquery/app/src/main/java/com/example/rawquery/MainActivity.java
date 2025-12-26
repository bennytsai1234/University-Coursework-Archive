package com.example.rawquery;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private SQLiteDatabase SQLdb;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        listView = findViewById(R.id.Listview);

        // 開啟或創建資料庫
        SQLdb = openOrCreateDatabase("test.db", MODE_PRIVATE, null);

        // 查詢資料
        String query = "SELECT * FROM table01";
        Cursor cursor = SQLdb.rawQuery(query, null);

        // 處理查詢結果
        List<String> dataList = new ArrayList<>();
        if (cursor.moveToFirst()) {
            do {
                int num = cursor.getInt(cursor.getColumnIndex("num"));
                String data = cursor.getString(cursor.getColumnIndex("data"));
                String result = "編號：" + num + "，資料：" + data;
                dataList.add(result);
            } while (cursor.moveToNext());
        }

        // 關閉 Cursor
        cursor.close();

        // 顯示結果
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, dataList);
        listView.setAdapter(adapter);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 關閉資料庫
        SQLdb.close();
    }
}
