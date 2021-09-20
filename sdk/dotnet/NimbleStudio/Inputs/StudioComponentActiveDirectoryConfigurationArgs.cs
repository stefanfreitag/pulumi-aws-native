// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Inputs
{

    public sealed class StudioComponentActiveDirectoryConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("computerAttributes")]
        private InputList<Inputs.StudioComponentActiveDirectoryComputerAttributeArgs>? _computerAttributes;
        public InputList<Inputs.StudioComponentActiveDirectoryComputerAttributeArgs> ComputerAttributes
        {
            get => _computerAttributes ?? (_computerAttributes = new InputList<Inputs.StudioComponentActiveDirectoryComputerAttributeArgs>());
            set => _computerAttributes = value;
        }

        [Input("directoryId")]
        public Input<string>? DirectoryId { get; set; }

        [Input("organizationalUnitDistinguishedName")]
        public Input<string>? OrganizationalUnitDistinguishedName { get; set; }

        public StudioComponentActiveDirectoryConfigurationArgs()
        {
        }
    }
}
