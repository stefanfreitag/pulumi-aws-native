// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail.Outputs
{

    /// <summary>
    /// An object that sets the public accessibility of objects in the specified bucket.
    /// </summary>
    [OutputType]
    public sealed class BucketAccessRules
    {
        /// <summary>
        /// A Boolean value that indicates whether the access control list (ACL) permissions that are applied to individual objects override the getObject option that is currently specified.
        /// </summary>
        public readonly bool? AllowPublicOverrides;
        /// <summary>
        /// Specifies the anonymous access to all objects in a bucket.
        /// </summary>
        public readonly string? GetObject;

        [OutputConstructor]
        private BucketAccessRules(
            bool? allowPublicOverrides,

            string? getObject)
        {
            AllowPublicOverrides = allowPublicOverrides;
            GetObject = getObject;
        }
    }
}
