// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Outputs
{

    /// <summary>
    /// A set of origins and methods (cross-origin access that you want to allow). You can add up to 100 rules to the configuration.
    /// </summary>
    [OutputType]
    public sealed class BucketCorsRule
    {
        /// <summary>
        /// Headers that are specified in the Access-Control-Request-Headers header.
        /// </summary>
        public readonly ImmutableArray<string> AllowedHeaders;
        /// <summary>
        /// An HTTP method that you allow the origin to execute.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.S3.BucketCorsRuleAllowedMethodsItem> AllowedMethods;
        /// <summary>
        /// One or more origins you want customers to be able to access the bucket from.
        /// </summary>
        public readonly ImmutableArray<string> AllowedOrigins;
        /// <summary>
        /// One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
        /// </summary>
        public readonly ImmutableArray<string> ExposedHeaders;
        /// <summary>
        /// A unique identifier for this rule.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The time in seconds that your browser is to cache the preflight response for the specified resource.
        /// </summary>
        public readonly int? MaxAge;

        [OutputConstructor]
        private BucketCorsRule(
            ImmutableArray<string> allowedHeaders,

            ImmutableArray<Pulumi.AwsNative.S3.BucketCorsRuleAllowedMethodsItem> allowedMethods,

            ImmutableArray<string> allowedOrigins,

            ImmutableArray<string> exposedHeaders,

            string? id,

            int? maxAge)
        {
            AllowedHeaders = allowedHeaders;
            AllowedMethods = allowedMethods;
            AllowedOrigins = allowedOrigins;
            ExposedHeaders = exposedHeaders;
            Id = id;
            MaxAge = maxAge;
        }
    }
}
