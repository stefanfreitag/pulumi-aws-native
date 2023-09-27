// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2.Outputs
{

    /// <summary>
    /// The ``Cors`` property specifies a CORS configuration for an API. Supported only for HTTP APIs. See [Configuring CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html) for more information.
    /// </summary>
    [OutputType]
    public sealed class ApiCors
    {
        /// <summary>
        /// Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.
        /// </summary>
        public readonly bool? AllowCredentials;
        /// <summary>
        /// Represents a collection of allowed headers. Supported only for HTTP APIs.
        /// </summary>
        public readonly ImmutableArray<string> AllowHeaders;
        /// <summary>
        /// Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.
        /// </summary>
        public readonly ImmutableArray<string> AllowMethods;
        /// <summary>
        /// Represents a collection of allowed origins. Supported only for HTTP APIs.
        /// </summary>
        public readonly ImmutableArray<string> AllowOrigins;
        /// <summary>
        /// Represents a collection of exposed headers. Supported only for HTTP APIs.
        /// </summary>
        public readonly ImmutableArray<string> ExposeHeaders;
        /// <summary>
        /// The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.
        /// </summary>
        public readonly int? MaxAge;

        [OutputConstructor]
        private ApiCors(
            bool? allowCredentials,

            ImmutableArray<string> allowHeaders,

            ImmutableArray<string> allowMethods,

            ImmutableArray<string> allowOrigins,

            ImmutableArray<string> exposeHeaders,

            int? maxAge)
        {
            AllowCredentials = allowCredentials;
            AllowHeaders = allowHeaders;
            AllowMethods = allowMethods;
            AllowOrigins = allowOrigins;
            ExposeHeaders = exposeHeaders;
            MaxAge = maxAge;
        }
    }
}
