Ampta::Application.routes.draw do
 
  resources :sessions
  resources :projects
  resources :users
  resources :tickets

  resources :projects do
    resources :tickets
  end

  get '/projects/:id' , to: 'projects#show'
  get '/users/:id' , to: 'users#show'
  get '/tickets/:id' , to: 'tickets#show'
  
  delete '/projects/:id' , to:'projects#destroy'
  delete '/tickets/:id' , to:'tickets#destroy'

  put '/projects/:id', to: 'projects#update'
  put '/tickets/:id', to: 'tickets#update'
  
  root :to => "sessions#login"
  
  match "login", :to => "sessions#login"
  match "login_attempt", :to => "sessions#login_attempt"
  match "logout", :to => "sessions#logout"
  match "home", :to => "sessions#home"
  match "sort", :to => "projects#sort" 
 

  # See how all your routes lay out with "rake routes"

end
