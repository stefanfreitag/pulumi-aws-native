// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint.Inputs
{

    public sealed class InAppTemplateOverrideButtonConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("buttonAction")]
        public Input<Pulumi.AwsNative.Pinpoint.InAppTemplateButtonAction>? ButtonAction { get; set; }

        [Input("link")]
        public Input<string>? Link { get; set; }

        public InAppTemplateOverrideButtonConfigurationArgs()
        {
        }
        public static new InAppTemplateOverrideButtonConfigurationArgs Empty => new InAppTemplateOverrideButtonConfigurationArgs();
    }
}
