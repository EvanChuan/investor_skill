source "https://rubygems.org"

# github-pages 已內含並「精確鎖版」jekyll-remote-theme (= 0.4.3) 與
# jekyll-seo-tag (= 2.8.0)。不可再單獨宣告這兩個 gem —— 未鎖版會讓 bundler
# 為了同時滿足最新版與 github-pages 的精確鎖版，反過來把 github-pages 整包
# 降級到 2017 年的舊版（jekyll 3.6.2），導致 jekyll-remote-theme 呼叫
# 舊版 jekyll-github-metadata 不存在的 global_munger 而崩潰。
# 兩個外掛的啟用由 _config.yml 的 plugins: 清單負責，無須寫在 Gemfile。
gem "github-pages", group: :jekyll_plugins

# Ruby 3.0 起 rexml 由 default gem 改為 bundled gem，bundle exec 下不會自動載入。
# 保留此行作為保險：舊版 kramdown 需要 rexml 卻未宣告該相依。
gem "rexml"

# Windows 平台
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
