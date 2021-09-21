// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Outputs
{

    [OutputType]
    public sealed class BucketWebsiteConfiguration
    {
        public readonly string? ErrorDocument;
        public readonly string? IndexDocument;
        public readonly Outputs.BucketRedirectAllRequestsTo? RedirectAllRequestsTo;
        public readonly ImmutableArray<Outputs.BucketRoutingRule> RoutingRules;

        [OutputConstructor]
        private BucketWebsiteConfiguration(
            string? errorDocument,

            string? indexDocument,

            Outputs.BucketRedirectAllRequestsTo? redirectAllRequestsTo,

            ImmutableArray<Outputs.BucketRoutingRule> routingRules)
        {
            ErrorDocument = errorDocument;
            IndexDocument = indexDocument;
            RedirectAllRequestsTo = redirectAllRequestsTo;
            RoutingRules = routingRules;
        }
    }
}
