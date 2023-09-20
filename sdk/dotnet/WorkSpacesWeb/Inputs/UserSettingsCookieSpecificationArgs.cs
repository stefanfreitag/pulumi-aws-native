// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpacesWeb.Inputs
{

    public sealed class UserSettingsCookieSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("domain", required: true)]
        public Input<string> Domain { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        public UserSettingsCookieSpecificationArgs()
        {
        }
        public static new UserSettingsCookieSpecificationArgs Empty => new UserSettingsCookieSpecificationArgs();
    }
}
