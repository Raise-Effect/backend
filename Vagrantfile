Vagrant.configure("2") do |config|    
    config.vm.box = "ubuntu/trusty64"
    config.vm.provider "virtualbox" do |v|
        v.cpus = 2        
    end
    config.vm.provision "shell",
        inline: "apt-get update"
    config.vm.provision "docker" do |d|
        d.pull_images "ubuntu"
        d.build_image "/vagrant",        
            args: "-t app-image"
        d.run "app-image",
            args: "-d -p 8080:8080"
    config.vm.network "forwarded_port", guest: 8080, host: 8080
  end
end
