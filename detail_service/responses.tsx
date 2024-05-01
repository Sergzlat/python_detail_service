typescript
namespace Bolt.NextdetailService.Api.Responses;

/// <summary>
///     Ответ на запрос данных о новой детали
/// </summary>
/// <param name="Id">Идентификатор</param>
/// <param name="FirstName">Наименование</param>
/// <param name="MiddleName">классификация</param>
/// <param name="LastName">Вид</param>
/// <param name="BirthDate">Дата изготовления</param>
/// <param name="CardId">Номер в классификации</param>
public record NextdetailGetResponse(long Id, string FirstName, string MiddleName, string LastName, DateTime BirthDate, string CardId);

namespace Bolt.NextdetailService.Api.Responses;

/// <summary>
///     Ответ на запрос регистрации новой детали
/// </summary>
/// <param name="Id">Идентификатор детали</param>
/// <param name="Email">Адрес электронной почты</param>
/// <param name="Message">Сообщение</param>
public record SignUpResponse(long Id, string Email, string Message);
