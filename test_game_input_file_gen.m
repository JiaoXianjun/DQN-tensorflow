%function test_game_input_file_gen
clear all;
close all;

filename = 'game_input_fake.bin'
fid = fopen(filename,'w');
if fid == -1
  disp('file create failed!');
  return;
end

period_sample = 8;
num_period = 1024;
a = zeros(1, num_period*period_sample) + ' ';
a(1:period_sample:end) = '<';
len = fwrite(fid, a, 'uint8');
disp([num2str(len) 'bytes written.']);

fclose(fid);
