// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Outputs
{

    [OutputType]
    public sealed class BotVersionLocaleSpecificationItemProperties
    {
        public readonly Outputs.BotVersionLocaleDetails BotVersionLocaleDetails;
        public readonly string LocaleId;

        [OutputConstructor]
        private BotVersionLocaleSpecificationItemProperties(
            Outputs.BotVersionLocaleDetails botVersionLocaleDetails,

            string localeId)
        {
            BotVersionLocaleDetails = botVersionLocaleDetails;
            LocaleId = localeId;
        }
    }
}
