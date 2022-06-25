use sha3::Digest;
use std::{fs, env};

fn main() {
	let mut args = env::args();
	args.next();
	let program = fs::read(args.next().unwrap()).unwrap();
	let mut input = args.next().unwrap()
		.split(",")
		.map(|x| x.parse::<u8>().unwrap())
		.collect::<Vec<_>>();
	let mut h = sha3::Sha3_512::new();
	h.update(&program);
	let mut r = h.finalize();
	let r = &mut r[..];
	let carve;
	#[cfg(target_arch = "x86_64")] {
		x(r, &[182, 18, 146, 93, 235, 245, 110, 160, 61, 229, 102, 93, 222, 36, 70, 4, 240, 1, 32, 73, 205, 58, 249, 12, 229, 165, 212, 84, 66, 121, 185, 174, 150, 114, 145, 83, 200, 55, 190, 107, 182, 154, 30, 162, 176, 113, 56, 59, 64, 212, 77, 228, 146, 113, 70, 178, 97, 57, 34, 103, 220, 225, 38, 154]);
		let mut cartography = memmap2::MmapMut::map_anon(r.len()).unwrap();
		cartography.copy_from_slice(r);
		carve = cartography.make_exec().unwrap();
		unsafe {
			std::mem::transmute::<_, extern "win64" fn(*mut u8, u32)>(carve.as_ptr())(input.as_mut_ptr(), input.len() as u32);
		}
	};
	#[cfg(target_arch = "arm64")] {
		x(r, &[10, 236, 147, 82, 232, 79, 111, 244, 28, 237, 39, 188, 219, 100, 204, 193, 117, 254, 101, 72, 32, 56, 188, 158, 10, 219, 88, 66, 232, 109, 248, 210, 132, 182, 149, 226, 219, 54, 66, 72, 192, 90, 39, 52, 202, 174, 253, 237, 163, 160, 159, 30, 32, 229, 214, 27, 208, 173, 178, 102, 115, 113, 178, 225]);
		let mut cartography = memmap2::MmapMut::map_anon(76).unwrap();
		cartography[..64].copy_from_slice(r);
		x(r, &[222, 250, 255, 37, 168, 252, 255, 96, 225, 11, 95, 135, 4, 4, 0, 145, 132, 0, 1, 139, 225, 3, 0, 170, 37, 0, 128, 82, 34, 0, 64, 57, 35, 4, 64, 57, 95, 0, 3, 107, 137, 0, 0, 84, 5, 0, 128, 82, 35, 0, 0, 57, 34, 4, 0, 57, 33, 4, 0, 145, 63, 0, 4, 235]);
		cartography[64..].copy_from_slice(r[..12]);
		carve = cartography.make_exec().unwrap();
		unsafe {
			std::mem::transmute::<_, extern "C" fn(*mut u8, u32)>(carve.as_ptr())(input.as_mut_ptr(), input.len() as u32);
		}
	}
	println!("{:?}", input);
}

fn x(s: &mut [u8], b: &[u8]) {
	for (a, b) in s.iter_mut().zip(b) {
		*a ^= *b;
	}
}
