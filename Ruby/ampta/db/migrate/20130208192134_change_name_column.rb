class ChangeNameColumn < ActiveRecord::Migration
  def change
  	rename_column :users, :encrypted_password, :password_confirmation 
 
  end
end

