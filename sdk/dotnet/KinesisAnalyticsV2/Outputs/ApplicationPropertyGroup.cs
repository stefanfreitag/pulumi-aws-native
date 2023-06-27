// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Outputs
{

    /// <summary>
    /// Property key-value pairs passed into an application.
    /// </summary>
    [OutputType]
    public sealed class ApplicationPropertyGroup
    {
        /// <summary>
        /// Describes the key of an application execution property key-value pair.
        /// </summary>
        public readonly string? PropertyGroupId;
        /// <summary>
        /// Describes the value of an application execution property key-value pair.
        /// </summary>
        public readonly object? PropertyMap;

        [OutputConstructor]
        private ApplicationPropertyGroup(
            string? propertyGroupId,

            object? propertyMap)
        {
            PropertyGroupId = propertyGroupId;
            PropertyMap = propertyMap;
        }
    }
}
