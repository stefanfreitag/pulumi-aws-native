// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Inputs
{

    /// <summary>
    /// AssociationConfig for body inspection
    /// </summary>
    public sealed class WebAclAssociationConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("requestBody")]
        private InputMap<Inputs.WebAclRequestBodyAssociatedResourceTypeConfigArgs>? _requestBody;
        public InputMap<Inputs.WebAclRequestBodyAssociatedResourceTypeConfigArgs> RequestBody
        {
            get => _requestBody ?? (_requestBody = new InputMap<Inputs.WebAclRequestBodyAssociatedResourceTypeConfigArgs>());
            set => _requestBody = value;
        }

        public WebAclAssociationConfigArgs()
        {
        }
        public static new WebAclAssociationConfigArgs Empty => new WebAclAssociationConfigArgs();
    }
}
