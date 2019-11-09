// Code generated by vfsgen; DO NOT EDIT.

package gen

import (
	"bytes"
	"compress/gzip"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	pathpkg "path"
	"time"
)

// templates statically implements the virtual filesystem provided to vfsgen.
var templates = func() http.FileSystem {
	fs := vfsgen۰FS{
		"/": &vfsgen۰DirInfo{
			name:    "/",
			modTime: time.Date(2019, 11, 9, 5, 12, 7, 543805274, time.UTC),
		},
		"/cloudformation.ts": &vfsgen۰CompressedFileInfo{
			name:             "cloudformation.ts",
			modTime:          time.Date(2019, 11, 9, 5, 12, 7, 543969895, time.UTC),
			uncompressedSize: 2546,

			compressedContent: []byte("\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\xbc\x95\x4b\x4f\xe4\x38\x14\x85\xf7\xf5\x2b\xae\x4a\x2c\xaa\x46\x99\xcc\x3e\x35\x05\x83\x58\xb1\x60\x28\xd1\xec\x5a\x2d\x64\x9c\x9b\xb4\x45\x62\x5b\x7e\xd0\x14\xc1\xff\xbd\x65\x3b\xef\xa2\x78\xa8\x5b\x5d\x1b\x12\xf3\xf9\xde\x73\x4e\x9c\x5c\x56\x4b\xa1\x0c\xfc\x05\x44\x83\xb4\x95\xad\x19\x14\x4a\xd4\xb0\xfc\x2f\xde\xfd\x13\xff\x2c\x37\x8b\x05\x15\x5c\x1b\xb8\xbb\xa3\x82\x17\xac\x84\x2d\x70\xfc\xd1\xee\x49\x2f\xc2\xda\x6a\x49\x2b\x61\xf3\x42\xa8\x9a\x18\x26\xf8\x72\xbd\x59\xe0\x53\x68\x10\x37\x2b\x2c\x99\xe0\xb0\xed\xab\xa4\x25\x9a\xd5\x32\x2e\x1f\xd0\xda\x10\xfa\x70\x00\x87\x55\xcf\x76\x30\xe3\x06\x55\x41\x28\xc2\x17\xff\xaf\x73\x55\x6a\x68\x16\x00\x10\x0b\x9c\x65\x9d\xc8\x4b\x2e\xad\xf9\x57\x1b\xc5\x78\x79\xba\x09\x44\xec\x7c\x8c\x70\x7d\x0f\x5a\x11\xad\x63\x7d\xc0\x27\x83\x3c\xef\xe2\x4a\x77\x4a\x3c\xb2\x1c\xd5\x0d\x6a\x61\x15\xc5\xb6\x77\xb0\xa0\x2c\x35\x42\xad\x38\xa9\x31\x83\x58\x36\x01\xa2\x4a\x9d\x0d\x5a\x13\x10\xd2\xe8\x41\x65\x57\xe7\x5a\xfa\x08\xf5\xba\xad\xd7\xd7\x04\xe6\x45\xea\xa9\x66\x0d\xdb\x11\xd7\x7b\xcf\x42\xb3\x34\x06\xf9\xf2\x02\x5e\x48\x32\xc1\xba\x00\x02\x17\x6f\x06\xc0\x6d\x16\xfd\xb5\xb6\x12\xd5\xc1\x03\x4e\x62\xc9\x56\x53\xb4\xb2\x8e\xd1\xba\x51\x7c\x85\xe5\xd4\xf3\x50\xa2\x39\xa7\x54\x58\x6e\x2e\xf3\xd5\xd4\xf7\x25\x7f\x14\x0f\xbd\xeb\x0c\x76\x4a\xd4\x4c\x63\xf7\x34\x5a\x7b\x0a\x8d\x55\xbc\xdb\xa3\x2c\x37\xac\xc6\x94\x85\xbd\x73\x75\x19\xe3\x39\x3e\x65\xe3\x9e\xcb\x04\x1a\xd7\xca\x4c\xcd\x77\xe4\xab\x95\x42\x9d\x01\xe1\xfb\x35\x6c\x4f\x41\xa1\x4e\x49\x07\xaf\x37\xc7\x2c\x3c\xeb\x4f\x89\xff\xfa\xed\x17\xe5\x3f\xeb\x0f\x09\x7f\xd6\x47\x25\x87\xe3\xf6\x47\x33\x6f\x3b\x7e\x44\xb8\x8e\xe8\x44\xfc\xf0\x56\xcf\x5e\x88\x56\x54\x8d\x86\xe4\xc4\x90\xd9\xeb\xad\xe3\xe1\xa3\x0a\x83\x9c\x9d\xa8\x18\xdd\xbf\xce\xe4\x58\xe1\x7b\x8c\x95\x39\x31\xf8\x3e\x71\x83\xb2\x22\xf4\x28\xe8\x16\x4d\xa3\x08\x2f\x11\x4e\xee\x12\x38\x31\x7b\x89\x90\x6d\x21\xbd\x11\xc2\xdc\xee\x25\x6a\xe7\x0e\x7d\x37\x4d\x00\xd3\xff\x49\x8d\xce\xb5\xb6\x9b\xe6\x6f\x18\x55\xaa\xb1\xbe\x47\xe5\x6b\x45\xf6\x2a\xdc\xfb\x72\x11\x6e\x81\xb6\x46\xd3\xb0\xa2\xdb\x93\xc6\x38\x49\xe5\xdc\x59\xd3\x20\xcf\x9d\xcb\x46\x1b\xbc\x2a\xe7\x36\x7d\xcf\x00\x04\x1f\xf1\x6a\xe2\xa7\x16\xb9\xad\xa2\xa3\xab\x70\x39\xf2\xe3\xbf\x0f\x5a\xb6\x7e\x22\x18\xd4\x84\xb5\x91\xad\x57\xe2\xe9\x71\xd4\x06\xf3\x2e\x27\x8f\x7f\x2c\xab\x4f\xe7\xf5\x1b\x33\x9b\xe6\x16\xbf\x87\x71\x6d\x58\x79\xd3\x74\x77\xea\x67\x96\xe3\x20\x9a\xd9\x9d\x4d\xa4\x0b\xab\x8d\xa8\x67\xf3\xc8\xff\xa4\xbd\xaf\x18\x05\x85\x24\x17\xbc\xda\x03\x31\x46\xb1\x7b\x6b\x70\x98\x26\xd7\xd6\xf8\x11\xd8\x35\x38\xef\x89\x68\xee\x74\x34\x11\x8e\x4f\x38\xa9\x84\x44\x65\x18\xea\x98\x5e\x28\xb5\xeb\x17\x8f\xa4\x38\xa3\x62\xc3\x04\x68\xc1\xaf\xe3\x47\x6b\xf6\x21\x98\x0f\xce\xa9\xed\x57\xc6\xe7\x67\x47\xa8\xff\xa5\x69\xba\x6a\x15\xf8\x01\xda\xb8\x75\x72\xc0\x0c\x76\xb3\xd1\xf5\x21\x37\x8e\xdb\xf2\x1c\x0b\xc6\x31\x9f\x62\xa3\xd3\x33\x1a\xba\x5d\x38\xb7\xe2\x01\xb9\x73\x6f\x4d\xdd\xe1\xa4\x4d\xcf\xdb\xf0\xe6\xfe\x0c\x00\x00\xff\xff\xa1\x91\x50\x64\xf2\x09\x00\x00"),
		},
	}
	fs["/"].(*vfsgen۰DirInfo).entries = []os.FileInfo{
		fs["/cloudformation.ts"].(os.FileInfo),
	}

	return fs
}()

type vfsgen۰FS map[string]interface{}

func (fs vfsgen۰FS) Open(path string) (http.File, error) {
	path = pathpkg.Clean("/" + path)
	f, ok := fs[path]
	if !ok {
		return nil, &os.PathError{Op: "open", Path: path, Err: os.ErrNotExist}
	}

	switch f := f.(type) {
	case *vfsgen۰CompressedFileInfo:
		gr, err := gzip.NewReader(bytes.NewReader(f.compressedContent))
		if err != nil {
			// This should never happen because we generate the gzip bytes such that they are always valid.
			panic("unexpected error reading own gzip compressed bytes: " + err.Error())
		}
		return &vfsgen۰CompressedFile{
			vfsgen۰CompressedFileInfo: f,
			gr:                        gr,
		}, nil
	case *vfsgen۰DirInfo:
		return &vfsgen۰Dir{
			vfsgen۰DirInfo: f,
		}, nil
	default:
		// This should never happen because we generate only the above types.
		panic(fmt.Sprintf("unexpected type %T", f))
	}
}

// vfsgen۰CompressedFileInfo is a static definition of a gzip compressed file.
type vfsgen۰CompressedFileInfo struct {
	name              string
	modTime           time.Time
	compressedContent []byte
	uncompressedSize  int64
}

func (f *vfsgen۰CompressedFileInfo) Readdir(count int) ([]os.FileInfo, error) {
	return nil, fmt.Errorf("cannot Readdir from file %s", f.name)
}
func (f *vfsgen۰CompressedFileInfo) Stat() (os.FileInfo, error) { return f, nil }

func (f *vfsgen۰CompressedFileInfo) GzipBytes() []byte {
	return f.compressedContent
}

func (f *vfsgen۰CompressedFileInfo) Name() string       { return f.name }
func (f *vfsgen۰CompressedFileInfo) Size() int64        { return f.uncompressedSize }
func (f *vfsgen۰CompressedFileInfo) Mode() os.FileMode  { return 0444 }
func (f *vfsgen۰CompressedFileInfo) ModTime() time.Time { return f.modTime }
func (f *vfsgen۰CompressedFileInfo) IsDir() bool        { return false }
func (f *vfsgen۰CompressedFileInfo) Sys() interface{}   { return nil }

// vfsgen۰CompressedFile is an opened compressedFile instance.
type vfsgen۰CompressedFile struct {
	*vfsgen۰CompressedFileInfo
	gr      *gzip.Reader
	grPos   int64 // Actual gr uncompressed position.
	seekPos int64 // Seek uncompressed position.
}

func (f *vfsgen۰CompressedFile) Read(p []byte) (n int, err error) {
	if f.grPos > f.seekPos {
		// Rewind to beginning.
		err = f.gr.Reset(bytes.NewReader(f.compressedContent))
		if err != nil {
			return 0, err
		}
		f.grPos = 0
	}
	if f.grPos < f.seekPos {
		// Fast-forward.
		_, err = io.CopyN(ioutil.Discard, f.gr, f.seekPos-f.grPos)
		if err != nil {
			return 0, err
		}
		f.grPos = f.seekPos
	}
	n, err = f.gr.Read(p)
	f.grPos += int64(n)
	f.seekPos = f.grPos
	return n, err
}
func (f *vfsgen۰CompressedFile) Seek(offset int64, whence int) (int64, error) {
	switch whence {
	case io.SeekStart:
		f.seekPos = 0 + offset
	case io.SeekCurrent:
		f.seekPos += offset
	case io.SeekEnd:
		f.seekPos = f.uncompressedSize + offset
	default:
		panic(fmt.Errorf("invalid whence value: %v", whence))
	}
	return f.seekPos, nil
}
func (f *vfsgen۰CompressedFile) Close() error {
	return f.gr.Close()
}

// vfsgen۰DirInfo is a static definition of a directory.
type vfsgen۰DirInfo struct {
	name    string
	modTime time.Time
	entries []os.FileInfo
}

func (d *vfsgen۰DirInfo) Read([]byte) (int, error) {
	return 0, fmt.Errorf("cannot Read from directory %s", d.name)
}
func (d *vfsgen۰DirInfo) Close() error               { return nil }
func (d *vfsgen۰DirInfo) Stat() (os.FileInfo, error) { return d, nil }

func (d *vfsgen۰DirInfo) Name() string       { return d.name }
func (d *vfsgen۰DirInfo) Size() int64        { return 0 }
func (d *vfsgen۰DirInfo) Mode() os.FileMode  { return 0755 | os.ModeDir }
func (d *vfsgen۰DirInfo) ModTime() time.Time { return d.modTime }
func (d *vfsgen۰DirInfo) IsDir() bool        { return true }
func (d *vfsgen۰DirInfo) Sys() interface{}   { return nil }

// vfsgen۰Dir is an opened dir instance.
type vfsgen۰Dir struct {
	*vfsgen۰DirInfo
	pos int // Position within entries for Seek and Readdir.
}

func (d *vfsgen۰Dir) Seek(offset int64, whence int) (int64, error) {
	if offset == 0 && whence == io.SeekStart {
		d.pos = 0
		return 0, nil
	}
	return 0, fmt.Errorf("unsupported Seek in directory %s", d.name)
}

func (d *vfsgen۰Dir) Readdir(count int) ([]os.FileInfo, error) {
	if d.pos >= len(d.entries) && count > 0 {
		return nil, io.EOF
	}
	if count <= 0 || count > len(d.entries)-d.pos {
		count = len(d.entries) - d.pos
	}
	e := d.entries[d.pos : d.pos+count]
	d.pos += count
	return e, nil
}
