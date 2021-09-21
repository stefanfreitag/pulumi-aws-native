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
    public sealed class BucketRedirectRule
    {
        public readonly string? HostName;
        public readonly string? HttpRedirectCode;
        public readonly string? Protocol;
        public readonly string? ReplaceKeyPrefixWith;
        public readonly string? ReplaceKeyWith;

        [OutputConstructor]
        private BucketRedirectRule(
            string? hostName,

            string? httpRedirectCode,

            string? protocol,

            string? replaceKeyPrefixWith,

            string? replaceKeyWith)
        {
            HostName = hostName;
            HttpRedirectCode = httpRedirectCode;
            Protocol = protocol;
            ReplaceKeyPrefixWith = replaceKeyPrefixWith;
            ReplaceKeyWith = replaceKeyWith;
        }
    }
}
