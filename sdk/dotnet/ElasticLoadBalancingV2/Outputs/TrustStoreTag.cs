// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancingV2.Outputs
{

    [OutputType]
    public sealed class TrustStoreTag
    {
        public readonly string Key;
        public readonly string Value;

        [OutputConstructor]
        private TrustStoreTag(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
