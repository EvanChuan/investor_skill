source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "jekyll-remote-theme"
gem "jekyll-seo-tag"

# Ruby 3.0 起 rexml 由 default gem 改為 bundled gem，bundle exec 下不會自動載入。
# kramdown 的 HTML parser 需要 rexml 但未宣告此相依，故必須在此明示。
gem "rexml"

# Windows 平台
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
