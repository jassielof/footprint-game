// Run with:
// zig build-exe -O ReleaseSmall main.zig
const std = @import("std");

pub fn main() void {
    const stdout = std.fs.File.stdout();
    stdout.writeAll("Hello, world!\n") catch {};
}
