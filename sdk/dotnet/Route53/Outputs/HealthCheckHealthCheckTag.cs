// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53.Outputs
{

    /// <summary>
    /// A key-value pair to associate with a resource.
    /// </summary>
    [OutputType]
    public sealed class HealthCheckHealthCheckTag
    {
        /// <summary>
        /// The key name of the tag.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// The value for the tag.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private HealthCheckHealthCheckTag(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
