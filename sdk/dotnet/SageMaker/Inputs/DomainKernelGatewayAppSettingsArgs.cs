// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// The kernel gateway app settings.
    /// </summary>
    public sealed class DomainKernelGatewayAppSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("customImages")]
        private InputList<Inputs.DomainCustomImageArgs>? _customImages;

        /// <summary>
        /// A list of custom SageMaker images that are configured to run as a KernelGateway app.
        /// </summary>
        public InputList<Inputs.DomainCustomImageArgs> CustomImages
        {
            get => _customImages ?? (_customImages = new InputList<Inputs.DomainCustomImageArgs>());
            set => _customImages = value;
        }

        /// <summary>
        /// The default instance type and the Amazon Resource Name (ARN) of the default SageMaker image used by the KernelGateway app.
        /// </summary>
        [Input("defaultResourceSpec")]
        public Input<Inputs.DomainResourceSpecArgs>? DefaultResourceSpec { get; set; }

        public DomainKernelGatewayAppSettingsArgs()
        {
        }
        public static new DomainKernelGatewayAppSettingsArgs Empty => new DomainKernelGatewayAppSettingsArgs();
    }
}
