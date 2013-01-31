class CreateUsers < ActiveRecord::Migration
  def change
    create_table :users do |t|

      t.string "first_name", :limit => 20
      t.string "last_name", :limit =>40
      t.string "email"
      t.string "password", :limit => 20

      t.timestamps
    end
  end
end
