class ProjectsController < ApplicationController

	def index
		@projects = Project.all
	end
	
	def show

		@project = Project.find(params[:id])
		@users_in_project = @project.users
		@tickets_for_project =@project.tickets

	end
end
