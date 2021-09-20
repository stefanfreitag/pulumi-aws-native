// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Outputs
{

    /// <summary>
    /// First level statement that contains conditions, such as ByteMatch, SizeConstraint, etc
    /// </summary>
    [OutputType]
    public sealed class WebACLStatement
    {
        public readonly Outputs.WebACLAndStatement? AndStatement;
        public readonly Outputs.WebACLByteMatchStatement? ByteMatchStatement;
        public readonly Outputs.WebACLGeoMatchStatement? GeoMatchStatement;
        public readonly Outputs.WebACLIPSetReferenceStatement? IPSetReferenceStatement;
        public readonly Outputs.WebACLLabelMatchStatement? LabelMatchStatement;
        public readonly Outputs.WebACLManagedRuleGroupStatement? ManagedRuleGroupStatement;
        public readonly Outputs.WebACLNotStatement? NotStatement;
        public readonly Outputs.WebACLOrStatement? OrStatement;
        public readonly Outputs.WebACLRateBasedStatement? RateBasedStatement;
        public readonly Outputs.WebACLRegexPatternSetReferenceStatement? RegexPatternSetReferenceStatement;
        public readonly Outputs.WebACLRuleGroupReferenceStatement? RuleGroupReferenceStatement;
        public readonly Outputs.WebACLSizeConstraintStatement? SizeConstraintStatement;
        public readonly Outputs.WebACLSqliMatchStatement? SqliMatchStatement;
        public readonly Outputs.WebACLXssMatchStatement? XssMatchStatement;

        [OutputConstructor]
        private WebACLStatement(
            Outputs.WebACLAndStatement? andStatement,

            Outputs.WebACLByteMatchStatement? byteMatchStatement,

            Outputs.WebACLGeoMatchStatement? geoMatchStatement,

            Outputs.WebACLIPSetReferenceStatement? iPSetReferenceStatement,

            Outputs.WebACLLabelMatchStatement? labelMatchStatement,

            Outputs.WebACLManagedRuleGroupStatement? managedRuleGroupStatement,

            Outputs.WebACLNotStatement? notStatement,

            Outputs.WebACLOrStatement? orStatement,

            Outputs.WebACLRateBasedStatement? rateBasedStatement,

            Outputs.WebACLRegexPatternSetReferenceStatement? regexPatternSetReferenceStatement,

            Outputs.WebACLRuleGroupReferenceStatement? ruleGroupReferenceStatement,

            Outputs.WebACLSizeConstraintStatement? sizeConstraintStatement,

            Outputs.WebACLSqliMatchStatement? sqliMatchStatement,

            Outputs.WebACLXssMatchStatement? xssMatchStatement)
        {
            AndStatement = andStatement;
            ByteMatchStatement = byteMatchStatement;
            GeoMatchStatement = geoMatchStatement;
            IPSetReferenceStatement = iPSetReferenceStatement;
            LabelMatchStatement = labelMatchStatement;
            ManagedRuleGroupStatement = managedRuleGroupStatement;
            NotStatement = notStatement;
            OrStatement = orStatement;
            RateBasedStatement = rateBasedStatement;
            RegexPatternSetReferenceStatement = regexPatternSetReferenceStatement;
            RuleGroupReferenceStatement = ruleGroupReferenceStatement;
            SizeConstraintStatement = sizeConstraintStatement;
            SqliMatchStatement = sqliMatchStatement;
            XssMatchStatement = xssMatchStatement;
        }
    }
}
