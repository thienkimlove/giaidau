### Default template for new project

* Using `CKeditor` as default


* For `slug` in model, we using `SiteSlug` for generate slug by language which unique by contents every time.

* If `settings.DEBUG` is `True`, we no need `collectstatic`. we also enable logging to console and in uWSGI log.

