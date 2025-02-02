// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmplifyUiBuilder.Inputs
{

    public sealed class FormInputValuePropertyArgs : global::Pulumi.ResourceArgs
    {
        [Input("bindingProperties")]
        public Input<Inputs.FormInputValuePropertyBindingPropertiesArgs>? BindingProperties { get; set; }

        [Input("concat")]
        private InputList<Inputs.FormInputValuePropertyArgs>? _concat;
        public InputList<Inputs.FormInputValuePropertyArgs> Concat
        {
            get => _concat ?? (_concat = new InputList<Inputs.FormInputValuePropertyArgs>());
            set => _concat = value;
        }

        [Input("value")]
        public Input<string>? Value { get; set; }

        public FormInputValuePropertyArgs()
        {
        }
        public static new FormInputValuePropertyArgs Empty => new FormInputValuePropertyArgs();
    }
}
