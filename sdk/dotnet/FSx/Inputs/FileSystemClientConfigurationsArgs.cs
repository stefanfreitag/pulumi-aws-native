// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx.Inputs
{

    public sealed class FileSystemClientConfigurationsArgs : global::Pulumi.ResourceArgs
    {
        [Input("clients")]
        public Input<string>? Clients { get; set; }

        [Input("options")]
        private InputList<string>? _options;
        public InputList<string> Options
        {
            get => _options ?? (_options = new InputList<string>());
            set => _options = value;
        }

        public FileSystemClientConfigurationsArgs()
        {
        }
        public static new FileSystemClientConfigurationsArgs Empty => new FileSystemClientConfigurationsArgs();
    }
}
