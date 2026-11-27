require 'yaml'
root = ARGV.fetch(0)
langs = %w[pt-BR en es it fr de]
forms = YAML.safe_load(File.read('_data/proposal_forms.yml'))
ui = YAML.safe_load(File.read('_data/proposal_ui.yml'))
def translations!(labels, langs)
  raise "Missing translation #{labels.inspect}" unless labels.is_a?(Hash) && langs.all? { |l| labels[l].is_a?(String) && !labels[l].strip.empty? }
end
ui.each_value { |labels| translations!(labels, langs) }
forms.each do |id, fields|
  raise "Duplicate field #{id}" unless fields.map { |f| f['id'] }.uniq.size == fields.size
  fields.each do |f|
    translations!(f['label'], langs)
    (f['options'] || []).each { |o| translations!(o['label'], langs) }
    raise "Duplicate option #{id}" unless (f['options'] || []).map { |o| o['value'] }.uniq.size == (f['options'] || []).size
  end
end
pages = Dir.glob("#{root}/servicos/**/*").select { |p| File.file?(p) && (p.end_with?('.html') || File.extname(p).empty?) && File.read(p).include?('rmb-proposal-form') }
raise "Expected at least five rendered forms" if pages.size < 5
pages.each do |p|
  html = File.read(p)
  %w[name email phone].each { |f| raise "Missing required #{f} in #{p}" unless html.match?(/<input[^>]+name="#{f}"[^>]+required/) }
  raise "Unexpected active submit #{p}" unless html.match?(/<button[^>]+type="submit"[^>]+disabled/)
end
puts "Proposal schemas and #{pages.size} rendered forms validated"
