class AddNotnullToTickets < ActiveRecord::Migration
  def change
  	change_column :tickets, :name, :varchar, :null => false
  	change_column :tickets, :description, :text, :null => false
  	change_column :tickets, :user_id, :integer, :null => false
  	change_column :tickets, :project_id, :integer, :null => false
  
  end
end
