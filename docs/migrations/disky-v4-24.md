---
icon: material/package-up
status: new
---

# DiSky v4.23 -> v4.24

DiSky v4.24 introduced some breaking changes to fit well with the new Components V2 system. This migration guide will help you update your DiSky scripts to be compatible with the new version.

## Attachments

!!! info "Input AND output attachments' behavior has been changed, converted into [File Uploads](../messages/file-uploads.md) to be more consistent with the new Components V2 system and Discord." 

Everywhere you would normally use a string or an SkImage's Image, you must now use a File Upload. This includes:

- Adding an attachment to a message (via builder or inline)
- Usage of an attachment in an embed (= when you do `attachment://XXX`, where `XXX` is the name of the file you specified in the file upload)
- Specifying an attachment in a reply/post effect

It is also mandatory all within the Components V2 system, like in the **File Upload** or **Media Gallery** components.