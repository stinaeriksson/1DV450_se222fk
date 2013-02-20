class ApplicationController < ActionController::Base
  protect_from_forgery


   protected 
			def authenticate_user
				unless session[:user_id]
					redirect_to(:controller => 'sessions', :action => 'login')
					return false
				else
					@current_user = User.find session[:user_id] 
					return true
				end
			end

			def save_login_state
				if session[:user_id]
					redirect_to(:controller => 'sessions', :action => 'home')
					return false
				else
					return true
				end
			end

			def home
			  	@id = @current_user.id

			  	@projects = @current_user.projects

			  	@admin_projects = Project.where("owner_id = ?", @id)
			  	
				@tickets_for_user = User.find(@id).tickets
					#@project = @current_user.projects.find(params[:id])
					#	@projects_for_user = User.find(@id).projects
  			end

  			def control_user
  				@id = @current_user.id
		
				@project = Project.find(params[:id])
				@users_project = @current_user.projects

				case
				when @current_user.projects.find_by_id(params[:id])
						return true

				when @id == @project.owner_id
					return true
					
				else
					redirect_to(:controller =>'projects', :action =>'index')
					return false

				end  
				
			end
  			 
end
