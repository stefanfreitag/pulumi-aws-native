// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmplifyUiBuilder.Inputs
{

    public sealed class FormInputBindingPropertiesValuePropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("model")]
        public Input<string>? Model { get; set; }

        public FormInputBindingPropertiesValuePropertiesArgs()
        {
        }
        public static new FormInputBindingPropertiesValuePropertiesArgs Empty => new FormInputBindingPropertiesValuePropertiesArgs();
    }
}
