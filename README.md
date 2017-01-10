# noisy-atom-portal
This is a web portal for the Noisy Atom company. It demonstrates some clever IoT technology and eCommerce platform capability with QR code generation and tracking built out the box.

The platofm is based on python django. It uses all the common django libs to develop a CMS type portal.
Added to this it also uses QR-Codes for generating QR code enabled sku's. 
The message bus (AMQP) is Celery. This is used for queuing messages to and from the client/server interfaces so that a QR code 
can dynamically route to a URI.
