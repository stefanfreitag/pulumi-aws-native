// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Inputs
{

    public sealed class WebAclRegexMatchStatementArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldToMatch", required: true)]
        public Input<Inputs.WebAclFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        [Input("regexString", required: true)]
        public Input<string> RegexString { get; set; } = null!;

        [Input("textTransformations", required: true)]
        private InputList<Inputs.WebAclTextTransformationArgs>? _textTransformations;
        public InputList<Inputs.WebAclTextTransformationArgs> TextTransformations
        {
            get => _textTransformations ?? (_textTransformations = new InputList<Inputs.WebAclTextTransformationArgs>());
            set => _textTransformations = value;
        }

        public WebAclRegexMatchStatementArgs()
        {
        }
        public static new WebAclRegexMatchStatementArgs Empty => new WebAclRegexMatchStatementArgs();
    }
}
