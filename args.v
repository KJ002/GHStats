module args

import flag

pub const version = '0.1.0'

pub fn flag_parser(args []string) &flag.FlagParser {
	mut fp := flag.new_flag_parser(args)
	fp.version = args.version
	fp.skip_executable()
	return fp
}
