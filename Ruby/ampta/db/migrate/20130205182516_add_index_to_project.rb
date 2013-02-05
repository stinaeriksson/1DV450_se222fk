class AddIndexToProject < ActiveRecord::Migration
  def change
  	add_column :projects, :owner_id, :interger
  	add_index :projects, :owner_id
  end
end
