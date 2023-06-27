// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    /// <summary>
    /// A collection of settings that apply to an RSessionGateway app.
    /// </summary>
    [OutputType]
    public sealed class DomainRSessionAppSettings
    {
        /// <summary>
        /// A list of custom SageMaker images that are configured to run as a KernelGateway app.
        /// </summary>
        public readonly ImmutableArray<Outputs.DomainCustomImage> CustomImages;
        public readonly Outputs.DomainResourceSpec? DefaultResourceSpec;

        [OutputConstructor]
        private DomainRSessionAppSettings(
            ImmutableArray<Outputs.DomainCustomImage> customImages,

            Outputs.DomainResourceSpec? defaultResourceSpec)
        {
            CustomImages = customImages;
            DefaultResourceSpec = defaultResourceSpec;
        }
    }
}
