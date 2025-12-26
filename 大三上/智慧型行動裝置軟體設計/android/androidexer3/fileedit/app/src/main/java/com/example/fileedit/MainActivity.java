package com.example.fileedit;

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
    private EditText cmd;
    private int n=1;
    private String item,str;
    private static String CREATE_TABLE = "CREATE TABLE table01(_id INTEGER PRIMARY KEY,num INTEGER,data TEXT)";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mylist = findViewById(R.id.Listview);
        myBtn = findViewById(R.id.button);
        cmd = findViewById(R.id.editTextText);

        myBtn.setOnClickListener(ClickListener);
        item="資料項目" + n;
        str = "INSERT INTO table01 (num,data) VALUES (" + n + ",'" + item + "')";
        cmd.setText(str);
        SQLdb=openOrCreateDatabase("test.db",MODE_PRIVATE,null);
        try {
            SQLdb.execSQL(CREATE_TABLE);
        }
        catch (Exception e)
        {
            UpdateAdapter();
        }

    }

    private void UpdateAdapter() {
        Cursor cursor = SQLdb.rawQuery("SELECT * FROM table01",null);
        if(cursor != null && cursor.getCount() >= 0)
        {
            SimpleCursorAdapter adapter = new SimpleCursorAdapter(this,
                    android.R.layout.simple_expandable_list_item_2,
                    cursor,
                    new String[] {"num","data"},
                    new int[] {android.R.id.text1,android.R.id.text2},0);
            mylist.setAdapter(adapter);
        }
    }

    private View.OnClickListener ClickListener = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            if(view.getId() == R.id.button)
            {
                try {
                    SQLdb.execSQL(cmd.getText().toString());
                    UpdateAdapter();
                    n++;
                    item = "資料項目" + n;
                    str = "INSERT INTO table01 (num,data) VALUES (" + n + ",'" + item + "')";
                    cmd.setText(str);
                    Toast.makeText(MainActivity.this, "資料新增完畢", Toast.LENGTH_SHORT).show();
                }
                catch (Exception e)
                {
                    Toast.makeText(MainActivity.this, "error", Toast.LENGTH_SHORT).show();
                }
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
