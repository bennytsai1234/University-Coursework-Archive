package com.example.selectsql;

import androidx.appcompat.app.AppCompatActivity;

import android.database.SQLException;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.text.style.UpdateAppearance;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.SimpleCursorAdapter;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private SQLiteDatabase SQLdb = null;
    private ListView mylist;
    private Button myBtn;
    private Button myBtn2;
    private EditText cmd;
    private int n=1;
    private String item,str;
    private Cursor cursor;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mylist = findViewById(R.id.Listview);
        myBtn = findViewById(R.id.button);
        myBtn2 = findViewById(R.id.button2);
        cmd = findViewById(R.id.editTextText);

        myBtn.setOnClickListener(ClickListener);
        myBtn2.setOnClickListener(ClickListener);
        SQLdb=openOrCreateDatabase("test.db",MODE_PRIVATE,null);
        try {
            SQLdb.execSQL("CREATE TABLE table01(_id INTEGER PRIMARY KEY,name TEXT,price INTEGER)");
            SQLdb.execSQL("INSERT INTO table01 (name,price) VALUES ('bna',600)");
            SQLdb.execSQL("INSERT INTO table01 (name,price) VALUES ('water',100)");
            SQLdb.execSQL("INSERT INTO table01 (name,price) VALUES ('milk',500)");
            SQLdb.execSQL("INSERT INTO table01 (name,price) VALUES ('toast',400)");
            SQLdb.execSQL("INSERT INTO table01 (name,price) VALUES ('papa',300)");
        }
        catch (Exception e)
        {
            cursor = getAll();
            UpdateAdapter(cursor);
        }

    }

    private Cursor getAll() {
        Cursor res=SQLdb.rawQuery("SELECT _id,_id||'.'||name pname,price FROM table01",null);
        return res;
    }

    private Cursor get(long rowid) throws SQLException{
        Cursor res=SQLdb.rawQuery("SELECT _id,_id||'.'||name pname,price FROM table01 WHERE _id="+rowid,null);
        if(res.getCount()>0)
        {
            res.moveToFirst();
        }
        else
        {
            Toast.makeText(this,"沒有資料",Toast.LENGTH_SHORT).show();
        }
        return res;
    }

    private void UpdateAdapter(Cursor cursor) {
        if(cursor != null && cursor.getCount() >= 0)
        {
            SimpleCursorAdapter adapter = new SimpleCursorAdapter(this,
                    android.R.layout.simple_expandable_list_item_2,
                    cursor,
                    new String[] {"pname","price"},
                    new int[] {android.R.id.text1,android.R.id.text2},0);
            mylist.setAdapter(adapter);
        }
    }

    private View.OnClickListener ClickListener = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            if(view.getId() == R.id.button) {
                long id = Integer.parseInt(cmd.getText().toString());
                cursor = get(id);
                UpdateAdapter(cursor);
            }
            else if (view.getId() == R.id.button2)
            {
                cursor=getAll();
                UpdateAdapter(cursor);
            }
        }
    };

    @Override
    protected void onDestroy() {
        super.onDestroy();
        SQLdb.execSQL("DROP TABLE table01");
        SQLdb.close();
    }
}