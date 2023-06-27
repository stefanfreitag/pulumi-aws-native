// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    public sealed class RuleGroupRegexPatternSetReferenceStatementArgs : global::Pulumi.ResourceArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        [Input("fieldToMatch", required: true)]
        public Input<Inputs.RuleGroupFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        [Input("textTransformations", required: true)]
        private InputList<Inputs.RuleGroupTextTransformationArgs>? _textTransformations;
        public InputList<Inputs.RuleGroupTextTransformationArgs> TextTransformations
        {
            get => _textTransformations ?? (_textTransformations = new InputList<Inputs.RuleGroupTextTransformationArgs>());
            set => _textTransformations = value;
        }

        public RuleGroupRegexPatternSetReferenceStatementArgs()
        {
        }
        public static new RuleGroupRegexPatternSetReferenceStatementArgs Empty => new RuleGroupRegexPatternSetReferenceStatementArgs();
    }
}
