class AddNotnullToProjects < ActiveRecord::Migration
  def change
  	change_column :projects, :name, :varchar, :null => false
  	change_column :projects, :description, :text, :null => false
  	change_column :projects, :start_date, :date, :null => false
  	change_column :projects, :end_date, :date, :null => false
  	change_column :projects, :owner_id, :interger, :null => false
  end
end
