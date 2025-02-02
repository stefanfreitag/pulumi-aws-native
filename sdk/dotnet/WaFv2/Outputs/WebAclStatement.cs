// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    /// <summary>
    /// First level statement that contains conditions, such as ByteMatch, SizeConstraint, etc
    /// </summary>
    [OutputType]
    public sealed class WebAclStatement
    {
        public readonly Outputs.WebAclAndStatement? AndStatement;
        public readonly Outputs.WebAclByteMatchStatement? ByteMatchStatement;
        public readonly Outputs.WebAclGeoMatchStatement? GeoMatchStatement;
        public readonly Outputs.WebAclIpSetReferenceStatement? IpSetReferenceStatement;
        public readonly Outputs.WebAclLabelMatchStatement? LabelMatchStatement;
        public readonly Outputs.WebAclManagedRuleGroupStatement? ManagedRuleGroupStatement;
        public readonly Outputs.WebAclNotStatement? NotStatement;
        public readonly Outputs.WebAclOrStatement? OrStatement;
        public readonly Outputs.WebAclRateBasedStatement? RateBasedStatement;
        public readonly Outputs.WebAclRegexMatchStatement? RegexMatchStatement;
        public readonly Outputs.WebAclRegexPatternSetReferenceStatement? RegexPatternSetReferenceStatement;
        public readonly Outputs.WebAclRuleGroupReferenceStatement? RuleGroupReferenceStatement;
        public readonly Outputs.WebAclSizeConstraintStatement? SizeConstraintStatement;
        public readonly Outputs.WebAclSqliMatchStatement? SqliMatchStatement;
        public readonly Outputs.WebAclXssMatchStatement? XssMatchStatement;

        [OutputConstructor]
        private WebAclStatement(
            Outputs.WebAclAndStatement? andStatement,

            Outputs.WebAclByteMatchStatement? byteMatchStatement,

            Outputs.WebAclGeoMatchStatement? geoMatchStatement,

            Outputs.WebAclIpSetReferenceStatement? ipSetReferenceStatement,

            Outputs.WebAclLabelMatchStatement? labelMatchStatement,

            Outputs.WebAclManagedRuleGroupStatement? managedRuleGroupStatement,

            Outputs.WebAclNotStatement? notStatement,

            Outputs.WebAclOrStatement? orStatement,

            Outputs.WebAclRateBasedStatement? rateBasedStatement,

            Outputs.WebAclRegexMatchStatement? regexMatchStatement,

            Outputs.WebAclRegexPatternSetReferenceStatement? regexPatternSetReferenceStatement,

            Outputs.WebAclRuleGroupReferenceStatement? ruleGroupReferenceStatement,

            Outputs.WebAclSizeConstraintStatement? sizeConstraintStatement,

            Outputs.WebAclSqliMatchStatement? sqliMatchStatement,

            Outputs.WebAclXssMatchStatement? xssMatchStatement)
        {
            AndStatement = andStatement;
            ByteMatchStatement = byteMatchStatement;
            GeoMatchStatement = geoMatchStatement;
            IpSetReferenceStatement = ipSetReferenceStatement;
            LabelMatchStatement = labelMatchStatement;
            ManagedRuleGroupStatement = managedRuleGroupStatement;
            NotStatement = notStatement;
            OrStatement = orStatement;
            RateBasedStatement = rateBasedStatement;
            RegexMatchStatement = regexMatchStatement;
            RegexPatternSetReferenceStatement = regexPatternSetReferenceStatement;
            RuleGroupReferenceStatement = ruleGroupReferenceStatement;
            SizeConstraintStatement = sizeConstraintStatement;
            SqliMatchStatement = sqliMatchStatement;
            XssMatchStatement = xssMatchStatement;
        }
    }
}
